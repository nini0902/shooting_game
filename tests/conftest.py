"""測試環境初始化：使用 headless 設定避免測試時開啟視窗。"""

import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
