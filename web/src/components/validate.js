const yup = require("yup");

export const validate = async (name, data) => {
  if (name === "Email") {
    try {
      await emailObj.validate({ Email: data });
      return "";
    } catch (err) {
      return err.message;
    }
  } else if (name === "Registration Number") {
    let regex = /^RA[0-9]{13}$/;
    if (!regex.test(data) || data === undefined) {
      return "Registration number must start with RA and should be 13 characters";
    }
    return "";
  } else if (name === "Github Id") {
    if (data === undefined) {
      return "Github Username is required";
    }
    const res = await github(data);
    if (res) {
      return "";
    }
    return "Github Id is not valid";
  } else {
    if (data.length === 0 || data === "") {
      return `${name} is required`;
    }
    return "";
  }
};

const github = async (data) => {
  const response = await fetch(`https://api.github.com/users/${data}`);
  const res = await response.json();
  return res["message"] === undefined;
};

export const emailObj = yup.object().shape({
  Email: yup.string().email().required(),
});
