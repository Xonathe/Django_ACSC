function update_button_state(){
      var dt = document.querySelector('input[id="frm_dt"]');
      var radio_button = document.querySelector('input[name="radio"]:checked');
      dt.disabled = radio_button.value != '2';
}