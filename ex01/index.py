def validate(cpf_param: str):
  CPF = cpf_param.replace(".", "").replace("-", "")
  
  if (CPF.isdigit() and len(CPF) == 11):
    return CPF
  
  return None

def separator(cpf_param: str) -> list[int]:
  cpf_list = []

  for index, value in enumerate(cpf_param):
    cpf_list.append(int(value))
    
    if (index == 8):
      return cpf_list
    

def calculate(cpf_param: str):
  count = 10
  accumulator = 0
  cpf_list = separator(cpf_param)

  for digit in enumerate(cpf_list):
    accumulator += digit[1] * count
    count -= 1
  
  accumulator = (accumulator * 10) % 11

  return accumulator

def execute():
  cpf_input = input("Informe o cpf: ")
  cpf_validated = validate(cpf_input)
  
  if(cpf_validated):
    result = calculate(cpf_validated)
    print(result)
  else:
    print("Insira um cpf válido!")


execute()

# cpf -> "529982247-25"

