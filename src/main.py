def ice_skating_price(day: str, is_member: bool):
    match day:
        case "T2" | "T3" | "T4" | "T5" | "T6":
            base_price = 170000
        case "T7" | "CN":
            base_price = 220000
        case _:
            return "Invalid"

    if is_member:
        return int(round(base_price * 0.8))
    return base_price


if __name__ == "__main__":
    day = input("Nhập ngày (T2 - CN): ").strip()
    member = input("Hội viên? (y/n): ").strip().lower() == 'y'
    price = ice_skating_price(day, member)
    print(f"{price:,} VNĐ" if price != "Invalid" else "Invalid")
