from pyngrok import ngrok

# --- THIS IS THE LINE YOU WRITE ---
# IMPORTANT: Change 8000 to the actual port your local server is using.
public_url = ngrok.connect(8000).public_url

print("✅ ngrok tunnel is live at:")
print(public_url)

# This keeps the script running so the tunnel stays open.
try:
    # Block forever so the tunnel stays open
    ngrok_process = ngrok.get_ngrok_process()
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print("Closing ngrok tunnel...")
    ngrok.kill()