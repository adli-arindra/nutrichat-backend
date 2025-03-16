import datetime
import firebase_admin
from firebase_admin import credentials, firestore

class Firebase:
    def __init__(self):
        cred = credentials.Certificate("app/firebase/admin.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def add_user(self, uid, nama, email, tanggal_lahir):
        user_ref = self.db.collection("user").document(uid)
        user_ref.set({
            "nama": nama,
            "email": email,
            "tanggal_lahir": tanggal_lahir
        })

    def update_user(self, uid, **kwargs):
        user_ref = self.db.collection("user").document(uid)
        user_ref.update(kwargs)

    def get_user(self, uid):
        user_ref = self.db.collection("user").document(uid).get()
        return user_ref.to_dict() if user_ref.exists else None

    def add_preassessment(self, uid, rutinitas, kondisi_medis, preferensi_makanan, alergi):
        pre_ref = self.db.collection("preassessment").document(uid)
        pre_ref.set({
            "rutinitas": rutinitas,
            "kondisi_medis": kondisi_medis,
            "preferensi_makanan": preferensi_makanan,
            "alergi": alergi
        })

    def update_preassessment(self, uid, **kwargs):
        pre_ref = self.db.collection("preassessment").document(uid)
        pre_ref.update(kwargs)

    def get_preassessment(self, uid):
        pre_ref = self.db.collection("preassessment").document(uid).get()
        return pre_ref.to_dict() if pre_ref.exists else None

    def add_kondisi(self, uid, berat_badan, tinggi_badan, kalori, karbohidrat, protein, lemak):
        kondisi_ref = self.db.collection("kondisi").document(uid)
        kondisi_ref.set({
            "berat_badan": berat_badan,
            "tinggi_badan": tinggi_badan,
            "kalori": kalori,
            "karbohidrat": karbohidrat,
            "protein": protein,
            "lemak": lemak
        })

    def update_kondisi(self, uid, **kwargs):
        kondisi_ref = self.db.collection("kondisi").document(uid)
        kondisi_ref.update(kwargs)

    def get_kondisi(self, uid):
        kondisi_ref = self.db.collection("kondisi").document(uid).get()
        return kondisi_ref.to_dict() if kondisi_ref.exists else None

    def CreatePrompt(self, uid):
        def calculate_age(dob):
            try:
                birth_date = datetime.strptime(dob, "%Y-%m-%d")
                today = datetime.today()
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                return age
            except ValueError:
                return "N/A"
        
        user_data = self.get_user(uid)
        preassessment_data = self.get_preassessment(uid)
        kondisi_data = self.get_kondisi(uid)

        if not user_data:
            return "User not found."

        prompt = f"User Profile:\n"
        prompt += f"Nama saya adalah {user_data.get('nama', 'N/A')}, "
        age = calculate_age(user_data.get('tanggal_lahir', 'N/A'))
        prompt += f"dan umur saya adalah {age} tahun\n\n"

        if preassessment_data:
            prompt += f"Rutinitas saya adalah {preassessment_data.get('rutinitas', 'N/A')}, "
            prompt += f"Riwayat medis saya {preassessment_data.get('kondisi_medis', 'N/A')}, "
            prompt += f"Preferensi makanan saya {preassessment_data.get('preferensi_makanan', 'N/A')}, "
            prompt += f"dan saya memiliki alergi terhadap {preassessment_data.get('alergi', 'N/A')}.\n\n"
        
        if kondisi_data:
            prompt += f"Berat saya {kondisi_data.get('berat_badan', 'N/A')} kg, "
            prompt += f"Tinggi saya {kondisi_data.get('tinggi_badan', 'N/A')} cm, "
            prompt += f"Calories: {kondisi_data.get('kalori', 'N/A')} kcal/day, "
            prompt += f"Carbohydrates: {kondisi_data.get('karbohidrat', 'N/A')} g, "
            prompt += f"Protein: {kondisi_data.get('protein', 'N/A')} g, "
            prompt += f"Fat: {kondisi_data.get('lemak', 'N/A')} g.\n"

        return prompt



if __name__ == "__main__":
    fb = Firebase()
    
    fb.add_user("123", "John Doe", "john@example.com", "1990-01-01")
    
    fb.update_user("123", email="john.doe@example.com")
    
    print(fb.get_user("123"))
    
    fb.add_preassessment("123", "Sedentary", "Diabetes", "Vegan", "Peanuts")
    
    print(fb.get_preassessment("123"))
    
    fb.add_kondisi("123", 70, 175, 2000, 250, 100, 50)
    
    print(fb.get_kondisi("123"))