from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentServer, AgentSession
from livekit.plugins import deepgram, elevenlabs, google, silero

from prompts import AGENT_INSTRUCTIONS
from tools import create_tattoo_lead


load_dotenv()


class TattooAssistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTIONS,
            tools=[create_tattoo_lead],
        )


server = AgentServer()


@server.rtc_session(agent_name="tattoo-agent")
async def tattoo_agent(ctx: agents.JobContext):
    session = AgentSession(
        llm=google.LLM(
            model="gemini-2.5-flash",
        ),
        stt=deepgram.STT(
            model="nova-3",
            language="en",
            punctuate=True,
            interim_results=True,
        ),
        tts=elevenlabs.TTS(
            model="eleven_multilingual_v2",
            voice_id="EXAVITQu4vr4xnSDxMaL",
        ),
        vad=silero.VAD.load(),
        preemptive_generation=False,
    )

    await session.start(
        room=ctx.room,
        agent=TattooAssistant(),
    )


if __name__ == "__main__":
    agents.cli.run_app(server)