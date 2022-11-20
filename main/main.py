
documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

def ask_doc_number():
  doc_number = input('Введите номер документа: ')
  return doc_number

def search_doc_in_base(doc_number, documents):
  for doc in documents:
    if doc_number == doc['number']:
      return doc
  print('Номер документа не найден в базе!')
  print()
  return False

def search_shelf_in_base(shelf, directories):
  if shelf in directories.keys():
    return True
  return False

def get_people_by_doc_number(doc_number, documents):
  for doc in documents:
    if doc['number'] == doc_number:
      people = doc['name']
      return people
  return False

def get_shelf_number(doc_number, directories):
  for shelf, docs in directories.items():
    if doc_number in docs:
      return shelf
  return False

def del_doc_in_base(doc, documents):
  if doc in documents:
    documents.remove(doc)
    return doc
  else:
    return False

def del_doc_to_shelf(doc_number, directories):
  for shelf_number, doc_by_shelf in directories.items():
    if doc_number in doc_by_shelf:
      doc_by_shelf.remove(doc_number)
      return shelf_number
  
def add_doc_to_shelf(doc_number, shelf, directories):
  for key_shelf, docs in directories.items():
    if key_shelf == shelf:
      docs.append(doc_number)
      return key_shelf

def ask_shelf_number():
  while True:
    shelf = input('Введите номер полки на которую будет помещен документ: ')
    search_result = search_shelf_in_base(shelf, directories)
    if search_result == True:
      break
    else:
      print('Указанный номер полки не существует в базе!')
  return shelf

while True:
  command = input('Введите команду: ')
  if command == 'p':
    doc_number = ask_doc_number()
    search_result = search_doc_in_base(doc_number, documents)
    if search_result != False:
      search_result = get_people_by_doc_number(doc_number, documents)
      print(f'Собственником документа является: {search_result}')
      print()
      
  elif command == 's':
    doc_number = ask_doc_number()
    search_result = search_doc_in_base(doc_number, documents)
    if search_result != False:
      search_shelf = get_shelf_number(doc_number, directories)
      if search_shelf != False:
        print(f"Документ '{search_result['type']} {search_result['number']} {search_result['name']}' находется на полке номер: {search_shelf}")
        print()
        
  elif command == 'l':
    print()
    print('В базе имеются следующие документы:')
    count = 1
    for doc in documents:
      print(f"{count}. {doc['type']} {doc['number']} {doc['name']}")
      count += 1
    print()

  elif command == 'a':
    print('Для добавление нового документа:')
    doc_type = input('Введите тип документа: ')
    doc_number = input('Введите номер документа: ')
    doc_name = input('Введите имя собственника документа: ')
    shelf = ask_shelf_number()
    doc_dict = {'type':doc_type, 'number':doc_number, 'name':doc_name}
    documents.append(doc_dict)
    add_to_shelf = add_doc_to_shelf(doc_number, shelf, directories)
    added_doc = search_doc_in_base(doc_number, documents)
    print()
    print(f"Документ '{added_doc['type']} {added_doc['number']} {added_doc['name']}' добавлен в базу данных!\nПоместите новый документ на полку номер: {add_to_shelf}")
    print()

  elif command == 'd':
    doc_number = ask_doc_number()
    search_result = search_doc_in_base(doc_number, documents)
    if search_result != False:
      delete_doc = del_doc_in_base(search_result, documents)
      shelf_number = del_doc_to_shelf(doc_number, directories)
      print(f"Документ '{delete_doc['type']} {delete_doc['number']} {delete_doc['name']}' удален!")
      print()

  elif command == 'm':
    doc_number = ask_doc_number()
    search_result = search_doc_in_base(doc_number, documents)
    if search_result != False:
      shelf_number = ask_shelf_number()
      del_to_shelf = del_doc_to_shelf(doc_number, directories)
      add_to_shelf = add_doc_to_shelf(doc_number, shelf_number, directories)
      print(f"Документ {search_result['type']} {search_result['number']} {search_result['name']} перемещен на полку номер: {add_to_shelf}")
      print()

  elif command == 'as':
    new_shelf = input('Введите номер новой полки: ')
    shelf_in_direc = search_shelf_in_base(new_shelf, directories)
    if shelf_in_direc == True:
      print(f'Полка с номером {new_shelf} уже существует в базе.')
      print()
    else:
      directories[new_shelf] = []
      print(f'Полка с номером {new_shelf} добавлена в базу')
      print()

  elif command == 'q':
    print()
    print('Сеанс завершен. Спасибо за использование нашего программного продукта!')
    break

  else:
    print()
    print('Введена неизвестная команда!')
    print()
    print('''Доступные команды:
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться;
    d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
    q – quit – выход из программы. ''')
    print()

