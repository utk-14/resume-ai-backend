import openai

openai.api_key = "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"
openai.base_url = "https://openrouter.ai/api/v1"

client = openai.OpenAI(api_key=openai.api_key, base_url=openai.base_url)

def list_models():
    resp = client.models.list()
    free = [m.id for m in resp.data if m.id.endswith(":free")]
    print("Free models:", free)
    return free

if __name__ == "__main__":
    list_models()
