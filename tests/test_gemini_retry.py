import unittest
from types import SimpleNamespace

from google.genai.errors import ServerError

from app.gemini_client import generate_text_with_retry


class GeminiRetryTests(unittest.TestCase):
    def test_retries_after_transient_503(self):
        calls = {"count": 0}

        def fake_generate_content(*args, **kwargs):
            calls["count"] += 1
            if calls["count"] < 3:
                raise ServerError(503, {"error": {"message": "temporarily unavailable"}}, None)
            return SimpleNamespace(text="Recovered workout plan")

        result = generate_text_with_retry(
            client=SimpleNamespace(models=SimpleNamespace(generate_content=fake_generate_content)),
            model_name="gemini-3.5-flash",
            prompt="test prompt",
            fallback_text="Fallback plan",
            max_retries=3,
            initial_delay=0,
        )

        self.assertEqual(result, "Recovered workout plan")
        self.assertEqual(calls["count"], 3)

    def test_returns_fallback_after_exhausting_retries(self):
        def fake_generate_content(*args, **kwargs):
            raise ServerError(503, {"error": {"message": "temporarily unavailable"}}, None)

        result = generate_text_with_retry(
            client=SimpleNamespace(models=SimpleNamespace(generate_content=fake_generate_content)),
            model_name="gemini-3.5-flash",
            prompt="test prompt",
            fallback_text="Fallback plan",
            max_retries=2,
            initial_delay=0,
        )

        self.assertEqual(result, "Fallback plan")


if __name__ == "__main__":
    unittest.main()
