import pathlib
import pygame
import random
from pyt2s.services import stream_elements


VOICE_MODEL = stream_elements.Voice.pt_PT_Wavenet_B.value 

RESPONSES_DIR: pathlib.Path = pathlib.Path("./responses/")
LOCKFILE: pathlib.Path = RESPONSES_DIR / "audio_playing.lock"

RESPONSES: dict[str, list[str]] = dict()


for response_file in RESPONSES_DIR.glob("*.txt"):
    with open(response_file, "r", encoding="utf-8") as file:
        name: str = response_file.name.removesuffix('.txt')
        content = file.read()
        RESPONSES[name] = content.splitlines()

pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)


def play_audio_file(audio_filepath: str) -> None:
    pygame.mixer.music.load(audio_filepath)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): pass


def play_event_audio(event_type: str, nsfw: bool = False) -> None:
    if audio_is_locked():
        print("[DEBUG] audio is locked")
        return

    lock_audio()

    print("[DEBUG] trying to play:", event_type)

    responses_list: list[str] = RESPONSES[event_type]
    if nsfw and (event_type + "_nsfw") in RESPONSES:
        responses_list.extend(RESPONSES[event_type + "_nsfw"])

    text: str = random.choice(responses_list)

    # print("nsfw:", nsfw)
    # print("responses_list:", responses_list)
    # print("text:", text)

    audio_data = stream_elements.requestTTS(text, VOICE_MODEL)

    with open("output.mp3", "wb") as f:
        f.write(audio_data)

    print("[DEBUG] playing text:", text)

    play_audio_file("output.mp3")

    unlock_audio()


def lock_audio():
    if LOCKFILE.exists():
        print("Lockfile exists. Another instance may be running.")
        return

    with open(LOCKFILE, "w") as f:
        f.write("playing")

def unlock_audio():
    if LOCKFILE.exists():
        LOCKFILE.unlink()

def audio_is_locked() -> bool:
    return LOCKFILE.exists()


def main():
    # play_audio_file("/home/fawkes/audio-test/audio.mp3")
    play_event_audio("blue_button", nsfw=False)


if __name__ == "__main__":
    main()

    
