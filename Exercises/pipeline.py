import os
import subprocess

# Đường dẫn đến thư mục gốc chứa các thư mục con "Exercise-1", "Exercise-2", ...
BASE_DIR = os.getcwd()

for i in range(1, 6):
    exercise_dir = os.path.join(BASE_DIR, f"Exercise-{i}")
    print("=" * 40)
    print(f"👉 Đang xử lý: {exercise_dir}")
    print("=" * 40)

    if not os.path.isdir(exercise_dir):
        print(f"❌ Không tìm thấy thư mục {exercise_dir}")
        continue

    try:
        # Bước 1: docker build
        print(f"🐳 Building Docker image: exercise-{i}")
        subprocess.run(["docker", "build", "--tag", f"exercise-{i}", "."], cwd=exercise_dir, check=True)

        # Bước 2: docker-compose up run
        print(f"🚀 Running docker-compose for exercise-{i}")
        subprocess.run(["docker-compose", "up", "run"], cwd=exercise_dir, check=True)

        print(f"✅ Hoàn thành Exercise-{i}\n")

    except subprocess.CalledProcessError as e:
        print(f"⚠️ Lỗi khi xử lý Exercise-{i}: {e}\n")

