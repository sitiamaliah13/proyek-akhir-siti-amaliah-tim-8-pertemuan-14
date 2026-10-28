
# Modul untuk menganalisis data nilai

def hitung_rata_rata(data):
    """Menghitung rata-rata nilai."""
    if len(data) == 0:
        return 0

    return sum(data) / len(data)


def cari_nilai_tertinggi(data):
    """Mencari nilai tertinggi."""
    if len(data) == 0:
        return None

    return max(data)


def cari_nilai_terendah(data):
    """Mencari nilai terendah."""
    if len(data) == 0:
        return None

    return min(data)
