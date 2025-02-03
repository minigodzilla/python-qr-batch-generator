import itertools
import subprocess

def generate_qr_codes():
    digits = ['0', '1', '2', '3']
    combinations = [''.join(p) for p in itertools.product(digits, repeat=4)]
    
    for code in combinations:
        url = f"https://craftii.net/retrieve?c={code}"
        filename = f"{code}.png"
        command = f'qr "{url}" > {filename}'
        
        print(f"Generating QR code for: {url}")
        subprocess.run(command, shell=True, check=True)
    
    print("All QR codes generated successfully.")

if __name__ == "__main__":
    generate_qr_codes()
