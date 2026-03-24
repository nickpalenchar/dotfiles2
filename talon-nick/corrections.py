from talon import Context

ctx = Context()

# Post-transcription find and replace
# These are case-insensitive and fire after Conformer transcribes
ctx.lists["user.vocabulary"] = {
    "web hook": "webhook",
    "web hooks": "webhooks",
    "git hub": "GitHub",
    "dynamo db": "DynamoDB",
    "type script": "TypeScript",
    "java script": "JavaScript",
    "node js": "Node.js",
    "dot env": "dotenv",
    "camel case": "camelCase",
    "snake case": "snake_case",
    "kebab case": "kebab-case",
    "pascal case": "PascalCase",
}
