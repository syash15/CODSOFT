contacts = []

def add_contact():
    print("\n🆕 --- Add Contact ---")
    name = input("👤 Enter name       : ")
    phone = input("📞 Enter phone     : ")
    email = input("📧 Enter email     : ")
    address = input("🏠 Enter address   : ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("✅ Contact added successfully!")

def view_contacts():
    print("\n📋 --- Contact List ---")
    if not contacts:
        print("⚠️  No contacts found.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"\n📇 Contact {idx}")
        print(f"👤 Name    : {contact['name']}")
        print(f"📞 Phone   : {contact['phone']}")
        print(f"📧 Email   : {contact['email']}")
        print(f"🏠 Address : {contact['address']}")

def search_contact():
    print("\n🔍 --- Search Contact ---")
    query = input("🔎 Enter name or phone: ")
    found = False
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print("\n✅ Contact Found:")
            print(f"👤 Name    : {contact['name']}")
            print(f"📞 Phone   : {contact['phone']}")
            print(f"📧 Email   : {contact['email']}")
            print(f"🏠 Address : {contact['address']}")
            found = True
            break
    if not found:
        print("❌ Contact not found.")

def update_contact():
    print("\n✏️ --- Update Contact ---")
    name = input("👤 Enter name to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("🛠️ Leave blank to keep current value.")
            phone = input("📞 New phone   : ")
            email = input("📧 New email   : ")
            address = input("🏠 New address : ")
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

def delete_contact():
    print("\n🗑️ --- Delete Contact ---")
    name = input("👤 Enter name to delete: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("🗑️ Contact deleted successfully!")
            return
    print("❌ Contact not found.")

def main():
    while True:
        print("\n📖 === Contact Book Menu ===")
        print("1️⃣  Add Contact")
        print("2️⃣  View Contacts")
        print("3️⃣  Search Contact")
        print("4️⃣  Update Contact")
        print("5️⃣  Delete Contact")
        print("6️⃣  Exit")

        choice = input("👉 Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

    input("\n🔚 Press Enter to exit...")  # Keeps window open on Windows

# Run the app
main()
