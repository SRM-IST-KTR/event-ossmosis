const yup = require("yup");

export const validate = async (name, data) => {
  switch (name) {
    case "College Email": {
      try {
        await emailSchema.validate(data);
        return "";
      } catch (err) {
        return "Email is malformed or missing!";
      }
    }

    case "Registration Number": {
      let regex = /^RA[0-9]{13}$/;
      if (!data || !regex.test(data)) {
        return "Registration Number starts with 'RA' with 13 characters!";
      }
      return "";
    }

    case "Github ID": {
      if (!data) {
        return "Github ID is required!";
      }
      const res = await validateGithubIdHandler(data);
      if (res) {
        return "";
      }
      return "Github ID is not valid!";
    }

    case "Project Link": {
      try {
        await linkSchema.validate(data);
        return "";
      } catch (err) {
        return "Link is either malformed or not a GitHub Link!";
      }
    }

    case "Validate E-mail": {
      if (data.length !== 6) {
        return "OTP should be of 6 digits!";
      } else {
        return "";
      }
    }

    default: {
      if (data.length === 0 || data === "") {
        return `${name} is required`;
      }
      return "";
    }
  }
};

const validateGithubIdHandler = async (data) => {
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
