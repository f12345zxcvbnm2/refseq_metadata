import argparse
import time
import csv
from Bio import Entrez


# 定义函数：获取单个 ID 的所有 metadata
def fetch_metadata(assembly_id, debug=False):
    try:
        # 搜索 Assembly ID
        handle = Entrez.esearch(db="assembly", term=assembly_id)
        record = Entrez.read(handle)
        handle.close()

        if not record["IdList"]:
            print(f"No record found for {assembly_id}")
            return None

        # 获取 Summary
        assembly_ncbi_id = record["IdList"][0]
        handle = Entrez.esummary(db="assembly", id=assembly_ncbi_id)
        summary = Entrez.read(handle)
        handle.close()
        return summary
    except Exception as e:
        if debug:
            print(f"Error fetching metadata for {assembly_id}: {e}")
        return None


def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="Fetch NCBI Assembly metadata.")
    parser.add_argument("-i", "--input", required=True, help="Input file containing assembly IDs (one per line).")
    parser.add_argument("-o", "--output", required=True, help="Output CSV file to save metadata.")
    parser.add_argument("-e", "--email", required=True, help="Email address for NCBI Entrez.")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode.")
    args = parser.parse_args()

    # 设置 Entrez 邮箱
    Entrez.email = args.email

    # 读取输入文件中的 Assembly IDs
    with open(args.input, "r") as f:
        ids = [line.strip() for line in f if line.strip()]  # 去掉空行

    # 初始化输出文件并写入表头
    with open(args.output, mode="w", newline="", encoding="utf-8") as f_out:
        csv_writer = csv.writer(f_out)
        header_written = False  # 确保表头只写一次

        for assembly_id in ids:
            print(f"Fetching metadata for {assembly_id}...")
            metadata = fetch_metadata(assembly_id, debug=args.debug)

            if metadata:
                for doc in metadata["DocumentSummarySet"]["DocumentSummary"]:
                    # 提取所有键值
                    if not header_written:
                        header = doc.keys()
                        csv_writer.writerow(header)  # 写入表头
                        header_written = True

                    # 写入每行数据
                    csv_writer.writerow([doc.get(key, "N/A") for key in header])

            # 防止被 NCBI 限制请求速度
            time.sleep(0.5)

    print(f"Metadata fetching complete! Output saved to {args.output}")


if __name__ == "__main__":
    main()
