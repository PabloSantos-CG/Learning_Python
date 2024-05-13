def calculate_distance():
  DISTANCE = float(input("Informe a distância percorrida: "))
  ticket = 0

  if(DISTANCE <= 200):
    ticket = DISTANCE * 0.5
    print(f"Valor final é: R$ {ticket:.2f}")
  else:
    ticket = DISTANCE * 0.35
    print(f"Valor final é: R$ {ticket:.2f}")

calculate_distance()

def calculate_salary():
  salary = float(input("Informe seu salário: "))
  increase = 0

  if(salary >= 1.250):
    increase = salary * 0.10
    salary += increase
    print(f"\nValor final é: R$ {salary:.2f} \nAumento de: R$ {increase}")
  
  else:
    increase = salary * 0.15
    increase += salary
    print(f"\nValor final é: R$ {salary:.2f} \nAumento de: R$ {increase}")

calculate_salary()