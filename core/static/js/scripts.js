    function validarSenha(senha) {
      // Verifica se a senha tem pelo menos 8 caracteres.
      if (senha.length < 8) {
        return false;
      }

      // Verifica se a senha inclui uma combinação de letras maiúsculas, minúsculas, números e símbolos.
      const containsUpperCase = /[A-Z]/.test(senha);
      const containsLowerCase = /[a-z]/.test(senha);
      const containsNumber = /[0-9]/.test(senha);
      const containsSymbol = /[!@#$%^&*()_+{}|:<>?~]/.test(senha);

      if (!containsUpperCase || !containsLowerCase || !containsNumber || !containsSymbol) {
        return false;
      }

      return true;
    }

    // Evento de envio do formulário

    const form = document.querySelector("form");

    form.addEventListener("submit", (event) => {
      // Obtém a senha do formulário
      const senha = document.querySelector("input[name='senha']").value;

      // Valida a senha
      const valida = validarSenha(senha);

      // Mostra uma mensagem de erro se a senha não for válida
      if (!valida) {
        event.preventDefault();
        alert("A senha deve ter pelo menos 8 caracteres e incluir uma combinação de letras maiúsculas, minúsculas, números e símbolos.");
      }
    });