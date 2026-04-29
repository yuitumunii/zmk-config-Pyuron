#!/usr/bin/env python3
import json
import time
import uuid
from pathlib import Path

LOG_PATH = Path("/Users/yuitumunii/ClaudeCompany/.cursor/debug-5ed579.log")
SESSION_ID = "5ed579"


def write_log(run_id: str, hypothesis_id: str, location: str, message: str, data: dict) -> None:
    payload = {
        "sessionId": SESSION_ID,
        "id": f"log_{int(time.time() * 1000)}_{uuid.uuid4().hex[:8]}",
        "timestamp": int(time.time() * 1000),
        "runId": run_id,
        "hypothesisId": hypothesis_id,
        "location": location,
        "message": message,
        "data": data,
    }
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=True) + "\n")


def yn(prompt: str) -> bool:
    while True:
        value = input(prompt).strip().lower()
        if value in {"y", "yes"}:
            return True
        if value in {"n", "no"}:
            return False
        print("Please answer y or n.")


def main() -> None:
    run_id = f"run-{int(time.time())}"
    print("Pyuron freeze capture started.")
    print("1) Start using the keyboard normally.")
    print("2) When freeze happens, return here and press Enter.")
    input("Press Enter to mark freeze timestamp...")

    # #region agent log H0
    write_log(
        run_id=run_id,
        hypothesis_id="H0",
        location="collect_pyuron_freeze_report.py:main",
        message="Freeze moment marked by user",
        data={},
    )
    # #endregion

    mouse_led = yn("At freeze moment, was automouse LED active? (y/n): ")
    host_connected = yn("Was host Bluetooth connection still shown as connected? (y/n): ")
    left_keys_work = yn("Did left half keys still work? (y/n): ")
    right_keys_work = yn("Did right half keys still work? (y/n): ")
    cursor_moves = yn("Did trackball still move cursor? (y/n): ")
    right_reboot_fix = yn("Did right-half reboot recover immediately? (y/n): ")

    # #region agent log H1
    write_log(
        run_id=run_id,
        hypothesis_id="H1",
        location="collect_pyuron_freeze_report.py:main",
        message="Split-link failure check",
        data={
            "leftKeysWork": left_keys_work,
            "rightKeysWork": right_keys_work,
            "rightRebootFix": right_reboot_fix,
        },
    )
    # #endregion

    # #region agent log H2
    write_log(
        run_id=run_id,
        hypothesis_id="H2",
        location="collect_pyuron_freeze_report.py:main",
        message="Host link failure check",
        data={"hostConnected": host_connected},
    )
    # #endregion

    # #region agent log H3
    write_log(
        run_id=run_id,
        hypothesis_id="H3",
        location="collect_pyuron_freeze_report.py:main",
        message="Automouse lock check",
        data={"automouseLed": mouse_led, "cursorMoves": cursor_moves},
    )
    # #endregion

    # #region agent log H4
    write_log(
        run_id=run_id,
        hypothesis_id="H4",
        location="collect_pyuron_freeze_report.py:main",
        message="Right-half runtime fault check",
        data={
            "rightKeysWork": right_keys_work,
            "cursorMoves": cursor_moves,
            "rightRebootFix": right_reboot_fix,
        },
    )
    # #endregion

    print("Capture complete. Logs written to:", LOG_PATH)


if __name__ == "__main__":
    main()
