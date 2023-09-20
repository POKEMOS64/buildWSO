function input(){
  if (input.checkValidity()) {
    input.classList.add('text-field__input_valid');
    input.nextElementSibling.textContent = 'Отлично!';
  } else {
    input.classList.add('text-field__input_invalid');
    input.nextElementSibling.textContent = input.validationMessage;
  }
}

