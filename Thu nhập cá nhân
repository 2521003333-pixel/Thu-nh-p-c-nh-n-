def tinh_thue_tncn(luong_gross, so_nguoi_phu_thuoc=0):
    """
    Hàm tính thuế thu nhập cá nhân (TNCN) theo tháng.
    Dữ liệu đầu vào:
    - luong_gross: Tiền lương tổng chưa trừ bảo hiểm, thuế (đơn vị: VNĐ)
    - so_nguoi_phu_thuoc: Số lượng người phụ thuộc (mặc định là 0)
    """
    
    # 1. Tính các khoản bảo hiểm bắt buộc (Hình 3: Người lao động đóng tổng cộng 10.5%)
    # Gồm: BHXH (8%), BHTN (1%), BHYT (1.5%)
    tien_bao_hiem = luong_gross * 0.105
    
    # 2. Các khoản giảm trừ gia cảnh (Hình 2)
    giam_tru_ban_than = 15500000  # 15.5 triệu đồng/tháng
    giam_tru_phu_thuoc = so_nguoi_phu_thuoc * 6200000  # 6.2 triệu đồng/người/tháng
    tong_giam_tru = giam_tru_ban_than + giam_tru_phu_thuoc
    
    # 3. Tính thu nhập tính thuế (TNTT)
    thu_nhap_tinh_thue = luong_gross - tien_bao_hiem - tong_giam_tru
    
    # Nếu thu nhập tính thuế <= 0 thì không phải nộp thuế
    if thu_nhap_tinh_thue <= 0:
        thue_phai_nop = 0
        thu_nhap_net = luong_gross - tien_bao_hiem
        return thue_phai_nop, thu_nhap_net
    
    # 4. Tính thuế lũy tiến từng phần theo biểu thuế 5 bậc (Hình 1)
    # Đổi sang đơn vị Triệu đồng để dễ tính toán theo bảng
    tntt_trieu = thu_nhap_tinh_thue / 1000000
    thue_trieu = 0
    
    # Bậc 1: Đến 10 triệu (Thuế suất 5%)
    if tntt_trieu <= 10:
        thue_trieu += tntt_trieu * 0.05
    else:
        thue_trieu += 10 * 0.05
        
        # Bậc 2: Trên 10 đến 30 triệu (Thuế suất 10%)
        if tntt_trieu <= 30:
            thue_trieu += (tntt_trieu - 10) * 0.10
        else:
            thue_trieu += (30 - 10) * 0.10
            
            # Bậc 3: Trên 30 đến 60 triệu (Thuế suất 20%)
            if tntt_trieu <= 60:
                thue_trieu += (tntt_trieu - 30) * 0.20
            else:
                thue_trieu += (60 - 30) * 0.20
                
                # Bậc 4: Trên 60 đến 100 triệu (Thuế suất 30%)
                if tntt_trieu <= 100:
                    thue_trieu += (tntt_trieu - 60) * 0.30
                else:
                    thue_trieu += (100 - 60) * 0.30
                    
                    # Bậc 5: Trên 100 triệu (Thuế suất 35%)
                    thue_trieu += (tntt_trieu - 100) * 0.35

    thue_phai_nop = thue_trieu * 1000000
    thu_nhap_net = luong_gross - tien_bao_hiem - thue_phai_nop
    
    return round(thue_phai_nop), round(thu_nhap_net)

# --- VÍ DỤ CHẠY THỬ ---
luong_thu_nghiem = 80000000  # 80 triệu đồng
nguoi_phu_thuoc = 1          # 1 người phụ thuộc

thue, net = tinh_thue_tncn(luong_thu_nghiem, nguoi_phu_thuoc)

print(f"Lương Gross: {luong_thu_nghiem:,} VNĐ")
print(f"Số người phụ thuộc: {nguoi_phu_thuoc}")
print("-" * 30)
print(f"Thuế TNCN phải nộp: {thue:,} VNĐ")
print(f"Lương Net nhận về:  {net:,} VNĐ")
