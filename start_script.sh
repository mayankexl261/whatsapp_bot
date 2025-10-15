sudo apt update -y
sudo apt-get update -y

sudo apt-get install -y python3 python3-pip python3.12-venv

if [ ! -d "myenv" ]; then
  python3 -m venv myenv
fi

source myenv/bin/activate

pip install --upgrade pip


pip install fastapi uvicorn nest-asyncio pyngrok twilio pandas sentence-transformers faiss-cpu python-dotenv python-multipart
