#!/usr/bin/env python3

import os
import requests
from tqdm import tqdm
import subprocess

url = "https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-stable/microsoft-edge-stable_131.0.2903.63-1_amd64.deb"
downloads_path = os.path.expanduser("~/Downloads")
file_name = "microsoft_edge_setup.deb"
save_path = os.path.join(downloads_path, file_name)

def display_final_message():
    print("✨ You're all set! Thank you for using this script! 🎉")
    print(" ")

    print("📧 Email: josuezolakiousa@gmail.com")
    print("🌐 Website: https://github.com/josuezolakiomd/modern-linktree")
    print(" ")
    print("💻 Script developed by Josue Zolakio on 11/22/2024.\n")
    print("🛠️ Stay tuned for more awesome tools! 🚀\n")
    print("⚠️ To apply the changes, please log out or restart your system. 🔄")
    print("🔐 Logging out ensures that all configurations are properly updated. ✅\n")

def download_with_progress_bar(url, save_path):
    
    print("\n🚀 Starting the download process... ⏳\n")
    
    try:
        # Send a GET request to the URL
        
        print("🌐 Connecting to the server...")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise exception for bad status codes
        print("✅ Connection established!\n")

        # Get the total file size
        total_size = int(response.headers.get('content-length', 0))
        print(f"📦 File size: {total_size / 1024 / 1024:.2f} MB")

        # Use tqdm to show progress
        with open(save_path, 'wb') as file, tqdm(
            desc="📥 Downloading",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                bar.update(len(chunk))
                
        print(f"\n✅ File downloaded successfully to: {save_path} 🎉")
        print("🔍 You can now install Microsoft Edge with your preferred package manager!\n")
    except requests.exceptions.RequestException as req_err:
        print(f"❌ Error: Could not connect to the URL. {req_err}")
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")

def install_package(file_path):
    print("🛠️ Starting the installation process... ⏳")
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        print("📂 Please make sure the file was downloaded correctly.")
        return

    try:
        # Running the installation command
        print(f"📦 Found the package at: {file_path}")
        print("🔄 Installing the package using 'dpkg'...")

        # Run the installation command with subprocess
        result = subprocess.run(
            ["sudo", "dpkg", "-i", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Print the output
        if result.returncode == 0:
            print(f"\n✅ Installation completed successfully! 🎉\n")
            print("🌐 Microsoft Edge is now ready to use. 🚀\n")
            
            display_final_message()
        else:
            print(f"❌ Installation failed. 🐛")
            print(f"🛑 Error Details:\n{result.stderr}")
            print("📖 Try running 'sudo apt-get -f install' to resolve dependencies.")

    except Exception as e:
        print(f"❌ An unexpected error occurred during installation: {e}")
    finally:
        print("🔐 Make sure to run the application securely!")

download_with_progress_bar(url, save_path)

file_path = os.path.expanduser("~/Downloads/microsoft_edge_setup.deb")

install_package(file_path)


# https://www.microsoft.com/en-us/edge/business/download?form=MA13FJ

# sudo apt install python3-tqdm