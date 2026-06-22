import tkinter as tk
from tkinter import messagebox

def tinh_thue_tncn(luong_gong, so_nguoi_phu_thuoc=0):
    # 1. Định nghĩa các hằng số từ hình ảnh
    TI_LE_BH = 0.105  # 10.5% bảo hiểm bắt buộc người lao động đóng
    GIAM_TRU_BAN_THAN = 15500000  # 15.5 triệu VND
    GIAM_TRU_PHU_THUOC = 6200000  # 6.2 triệu VND/người

    # 2. Tính tiền bảo hiểm bắt buộc
    tien_bao_hiem = luong_gong * TI_LE_BH

    # 3. Tính tổng mức giảm trừ gia cảnh
    tong_giam_tru = GIAM_TRU_BAN_THAN + (so_nguoi_phu_thuoc * GIAM_TRU_PHU_THUOC)

    # 4. Tính thu nhập tính thuế
    thu_nhap_tinh_thue = luong_gong - tien_bao_hiem - tong_giam_tru
    if thu_nhap_tinh_thue < 0:
        thu_nhap_tinh_thue = 0

    # 5. Tính thuế lũy tiến theo Biểu thuế từng phần (Hình 2)
    bac_thue = [
        (10000000, 0.05),       # Bậc 1: Đến 10 triệu (5%)
        (30000000, 0.10),       # Bậc 2: Trên 10 - 30 triệu (10%)
        (60000000, 0.20),       # Bậc 3: Trên 30 - 60 triệu (20%)
        (100000000, 0.30),      # Bậc 4: Trên 60 - 100 triệu (30%)
        (float('inf'), 0.35)    # Bậc 5: Trên 100 triệu (35%)
    ]

    thue_phai_nop = 0
    con_lai = thu_nhap_tinh_thue
    muc_duoi_truoc = 0

    for moc, thue_suat in bac_thue:
        if con_lai <= 0:
            break
        han_muc_bac = moc - muc_duoi_truoc
        tien_tinh_thue_bac = min(con_lai, han_muc_bac)
        thue_phai_nop += tien_tinh_thue_bac * thue_suat
        con_lai -= tien_tinh_thue_bac
        muc_duoi_truoc = moc

    # 6. Thu nhập thực nhận (Net)
    luong_net = luong_gong - tien_bao_hiem - thue_phai_nop

    return {
        "Luong_Gross": luong_gong,
        "Tien_Bao_Hiem": tien_bao_hiem,
        "Tong_Giam_Tru": tong_giam_tru,
        "Thu_Nhap_Tinh_Thue": thu_nhap_tinh_thue,
        "Thue_TNCN": thue_phai_nop,
        "Luong_Net": luong_net
    }

def ThucHienTinh():
    try:
        luong_gross = float(entry_luong.get().replace(',', ''))
        so_nguoi = int(entry_phuthuoc.get()) if entry_phuthuoc.get() else 0
        
        kq = tinh_thue_tncn(luong_gross, so_nguoi)
        
        lbl_bh_val.config(text=f"{kq['Tien_Bao_Hiem']:,.0f} VND")
        lbl_gt_val.config(text=f"{kq['Tong_Giam_Tru']:,.0f} VND")
        lbl_tntt_val.config(text=f"{kq['Thu_Nhap_Tinh_Thue']:,.0f} VND")
        lbl_thue_val.config(text=f"{kq['Thue_TNCN']:,.0f} VND")
        lbl_net_val.config(text=f"{kq['Luong_Net']:,.0f} VND", fg="green")
    except ValueError:
        messagebox.showerror("Lỗi dữ liệu", "Vui lòng nhập số hợp lệ!")

# --- Tạo giao diện đồ họa ---
root = tk.Tk()
root.title("Công cụ tính Thuế TNCN & Bảo Hiểm")
root.geometry("450x380")

tk.Label(root, text="Nhập lương Gross (VND):", font=("Arial", 11)).grid(row=0, column=0, padx=15, pady=10, sticky="w")
entry_luong = tk.Entry(root, font=("Arial", 11), width=20)
entry_luong.grid(row=0, column=1, padx=15, pady=10)
entry_luong.insert(0, "30,000,000")

tk.Label(root, text="Số người phụ thuộc:", font=("Arial", 11)).grid(row=1, column=0, padx=15, pady=10, sticky="w")
entry_phuthuoc = tk.Entry(root, font=("Arial", 11), width=20)
entry_phuthuoc.grid(row=1, column=1, padx=15, pady=10)
entry_phuthuoc.insert(0, "0")

btn_tinh = tk.Button(root, text="TÍNH TOÁN", font=("Arial", 11, "bold"), bg="#2196F3", fg="white", command=ThucHienTinh)
btn_tinh.grid(row=2, column=0, columnspan=2, pady=15)

# Hiển thị kết quả
labels = [
    ("Bảo hiểm bắt buộc (10.5%):", "lbl_bh_val"),
    ("Mức giảm trừ gia cảnh:", "lbl_gt_val"),
    ("Thu nhập tính thuế:", "lbl_tntt_val"),
    ("Thuế TNCN phải nộp:", "lbl_thue_val"),
    ("Lương NET thực nhận:", "lbl_net_val")
]

for i, (text, var_name) in enumerate(labels):
    tk.Label(root, text=text, font=("Arial", 10, "bold" if "NET" in text else "normal")).grid(row=3+i, column=0, padx=15, pady=6, sticky="w")
    lbl = tk.Label(root, text="0 VND", font=("Arial", 10, "bold" if "NET" in text else "normal"))
    lbl.grid(row=3+i, column=1, padx=15, pady=6, sticky="e")
    globals()[var_name] = lbl

ThucHienTinh()
root.mainloop()
    
