import random

def tro_choi_doan_so():
    print("=" * 30)
    print("CHÀO MỪNG ĐẾN VỚI TRÒ CHƠI ĐOÁN SỐ!")
    print("Máy tính đã chọn một số từ 1 đến 100.")
    print("=" * 30)

    # Máy tính chọn ngẫu nhiên một số
    so_bi_mat = random.randint(1, 100)
    so_lan_doan = 0
    da_doan_trung = False

    while not da_doan_trung:
        try:
            # Nhận đầu vào và tăng số lần thử
            du_doan = int(input("\nNhập con số bạn đoán (1-100): "))
            so_lan_doan += 1

            if du_doan < 1 or du_doan > 100:
                print("Lưu ý: Chỉ nhập số trong khoảng từ 1 đến 100 thôi nhé!")
                continue

            # Kiểm tra kết quả
            if du_doan < so_bi_mat:
                print("Thấp quá! Thử số lớn hơn xem.")
            elif du_doan > so_bi_mat:
                print("Cao quá! Thử số nhỏ hơn chút.")
            else:
                da_doan_trung = True
                print(f"\nCHÚC MỪNG! Bạn đã đoán đúng số {so_bi_mat}.")
                print(f"Bạn đã mất {so_lan_doan} lần để tìm ra đáp án.")

        except ValueError:
            print("Lỗi: Vui lòng chỉ nhập số nguyên, không nhập chữ hay ký tự đặc biệt!")

    print("\nCảm ơn bạn đã chơi. Hẹn gặp lại lần sau!")

# Gọi hàm để bắt đầu chơi
if __name__ == "__main__":
    tro_choi_doan_so()