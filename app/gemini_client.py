import time

from google.genai.errors import ServerError


def generate_text_with_retry(
    client,
    model_name,
    prompt,
    fallback_text,
    max_retries=3,
    initial_delay=2,
):

    for attempt in range(max_retries + 1):

        try:

            response = client.interactions.create(
                model=model_name,
                input=prompt,
            )

            if response and getattr(response, "output_text", None):
                return response.output_text

            return fallback_text

        except ServerError as exc:

            status_code = getattr(exc, "code", None)

            if status_code != 503 or attempt >= max_retries:
                return fallback_text

            wait_time = initial_delay * (2 ** attempt)

            time.sleep(wait_time)

        except Exception as exc:

            if getattr(exc, "code", None) == 429:
                return fallback_text

            if "429" in str(exc):
                return fallback_text

            if "rate limit" in str(exc).lower():
                return fallback_text

            return fallback_text

    return fallback_text