import psycopg2
import pandas as pd

def main():
    host = "postgres"
    database = "postgres"
    user = "postgres"
    pas = "postgres"

    # Kết nối đến PostgreSQL
    conn = psycopg2.connect(host=host, database=database, user=user, password=pas)
    cur = conn.cursor()

    # Map CSV và tên bảng
    csv_table_map = {
        "data/products.csv": "products",
        "data/transactions.csv": "transactions",
        "data/accounts.csv": "accounts"
    }

    for file_path, table_name in csv_table_map.items():
        df = pd.read_csv(file_path)

        # Tạo bảng (tất cả cột kiểu TEXT cho đơn giản)
        columns = ', '.join([f'"{col}" TEXT' for col in df.columns])
        cur.execute(f'DROP TABLE IF EXISTS {table_name};')
        cur.execute(f'CREATE TABLE {table_name} ({columns});')

        # Insert dữ liệu
        for _, row in df.iterrows():
            placeholders = ', '.join(['%s'] * len(row))
            sql = f'INSERT INTO {table_name} VALUES ({placeholders});'
            cur.execute(sql, tuple(row))

            # In ra dòng dữ liệu đã chèn
            print(f"Đã chèn: {tuple(row)} vào bảng '{table_name}'")

        print(f"✅ Đã chèn dữ liệu vào bảng '{table_name}'")

    conn.commit()
    cur.close()
    conn.close()
    print("🎉 Dữ liệu đã được insert thành công vào PostgreSQL.")

if __name__ == "__main__":
    main()
