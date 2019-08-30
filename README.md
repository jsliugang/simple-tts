# simple-tts

A simple TTS library using your OS-native (offline) TTS engine (i.e. SAPI on Windows).

This library is intentionally written to be as small and simple as possible, in order to serve as a clear reference on how to easily use OS-native TTS engines from Python.

Currently, this package only supports Windows (via `SAPI`, using `win32com.client`).
Contributions to enable TTS support on macOS/OSX and Linux is welcome.


