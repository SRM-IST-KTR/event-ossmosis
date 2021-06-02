const yup = require("yup");

export const validate = async (name, data) => {
  console.log(name);
  if (name === "College Email") {
    try {
      console.log(data);
      await emailSchema.validate(data);
      return "";
    } catch (err) {
      return "Email is malformed or missing!";
    }
  } else if (name === "Registration Number") {
    let regex = /^RA[0-9]{13}$/;
    if (!regex.test(data) || data === undefined) {
      return "Registration number must start with RA and should be 13 characters!";
    }
    return "";
  } else if (name === "Github Id") {
    if (data === undefined) {
      return "Github Username is required!";
    }
    const res = await github(data);
    if (res) {
      return "";
    }
    return "Github ID is not valid!";
  } else if (name === "Project Link") {
    try {
      await linkSchema.validate(data);
      return "";
    } catch (err) {
      return "Link is either malformed or not a GitHub Link!";
    }
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

export const emailSchema = yup.string().trim().email().required();

export const linkSchema = yup
  .string()
  .trim()
  .url()
  .matches(/^https:\/\/github.com\/[\w|\D]+\/[\w|\D]+$/)
  .required();
