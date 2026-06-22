import streamlit as st

st.set_page_config(
    page_title="Tính Thuế TNCN - Ngọc Trinh",
    page_icon="💰"
)

st.title("💰 Ứng dụng tính Thuế Thu Nhập Cá Nhân - Ngọc Trinh")

# Nhập dữ liệu
luong = st.number_input(
    "Nhập thu nhập hàng tháng (VNĐ):",
    min_value=0.0,
    step=1000000.0
)

nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc:",
    min_value=0,
    step=1
)

if st.button("Tính thuế"):
    
    # Tính bảo hiểm người lao động 10.5%
    bao_hiem = luong * 10.5 / 100

    # Giảm trừ gia cảnh
    giam_tru_ban_than = 15500000
    giam_tru_phu_thuoc = nguoi_phu_thuoc * 6200000

    tong_giam_tru = (
        giam_tru_ban_than + giam_tru_phu_thuoc
    )

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = (
        luong - bao_hiem - tong_giam_tru
    )

    if thu_nhap_tinh_thue <= 0:
        thue = 0
    else:
        thue = 0

        bac_thue = [
            (10000000, 0.05),
            (30000000, 0.10),
            (60000000, 0.20),
            (100000000, 0.30),
            (float("inf"), 0.35)
        ]

        muc_duoi = 0

        for muc_tren, ty_le in bac_thue:
            if thu_nhap_tinh_thue > muc_duoi:
                phan_thu_nhap = min(
                    thu_nhap_tinh_thue,
                    muc_tren
                ) - muc_duoi

                thue += phan_thu_nhap * ty_le

                muc_duoi = muc_tren
            else:
                break

    luong_thuc_nhan = luong - bao_hiem - thue

    st.success("KẾT QUẢ TÍNH THUẾ")

    st.write(
        f"💵 Thu nhập trước thuế: {luong:,.0f} VNĐ"
    )
    st.write(
        f"🏥 Bảo hiểm phải đóng (10.5%): {bao_hiem:,.0f} VNĐ"
    )
    st.write(
        f"👨 Giảm trừ bản thân: {giam_tru_ban_than:,.0f} VNĐ"
    )
    st.write(
        f"👨‍👩‍👧 Người phụ thuộc: {giam_tru_phu_thuoc:,.0f} VNĐ"
    )
    st.write(
        f"📊 Thu nhập tính thuế: {max(0, thu_nhap_tinh_thue):,.0f} VNĐ"
    )
    st.write(
        f"💰 Thuế TNCN phải nộp: {thue:,.0f} VNĐ"
    )
    st.write(
        f"✅ Lương thực nhận: {luong_thuc_nhan:,.0f} VNĐ"
    )
