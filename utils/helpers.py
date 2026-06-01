"""Helper functions"""

def format_time(seconds):
    """Format seconds into readable time"""
    days = int(seconds // 86400)
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    return f"{days}d {hours}h {minutes}m {secs}s"