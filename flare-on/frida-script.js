Java.perform(function() {
    Java.use("com.fireeye.flarebear.FlareBearActivity").getPassword.implementation = function() {
        console.log("Inside getPassword function");
        const password = this.getPassword();
        console.log("Password: " + password);
        return password;
    };

});