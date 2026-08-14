RATE_LIMITS = {
    "auth": {"requests": 10, "window_seconds": 60},
    "otp": {"requests": 5, "window_seconds": 300},
    "verification": {"requests": 30, "window_seconds": 60},
    "general": {"requests": 120, "window_seconds": 60},
}
