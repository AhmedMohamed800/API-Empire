import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import { createContext } from "react";

type FormIN = {
  email: string;
  password: string;
  remember_me: boolean;
};

export function useFormIN() {
  const [form, setForm] = useState<FormIN>({
    email: "",
    password: "",
    remember_me: false,
  });

  const [error, setError] = useState<string>("");
  const navigate = useNavigate();

  async function submitForm(e: any): Promise<void> {
    e.preventDefault();
    setError("");
    if (!form.email || !form.password) {
      return;
    }

    const LOGINURL = `${process.env.REACT_APP_API_URL}/api/v1/login`;
    try {
      const response = await axios.post(
        LOGINURL,
        {
          email: form.email,
          password: form.password,
          remember_me: form.remember_me,
        },
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        },
      );
      const { session } = response.data;
      Cookies.set("session", JSON.stringify(session));
      navigate("/APIs");
    } catch (error) {
      if (error.response) {
        setError(error.response.data.error);
      } else {
        setError(error.message);
      }
    }
  }

  function handleForm(e: React.ChangeEvent<HTMLInputElement>): void {
    const id = e.target.id;
    const value =
      e.target.type === "checkbox" ? e.target.checked : e.target.value;
    setForm({ ...form, [id]: value });
  }

  return { form, error, handleForm, submitForm };
}

type FormUP = {
  first_name: string;
  last_name: string;
  email: string;
  password: string;
};

export function useFormUP() {
  const [form, setForm] = useState<FormUP>({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  });

  const [error, setError] = useState<string>("");
  const navigate = useNavigate();

  async function submitForm(e: any): Promise<void> {
    e.preventDefault();
    setError("");
    if (!form.email || !form.password || !form.first_name || !form.last_name) {
      return;
    }

    const LOGINURL = `${process.env.REACT_APP_API_URL}/api/v1/user`;
    try {
      const response = await axios.post(
        LOGINURL,
        {
          email: form.email,
          password: form.password,
          last_name: form.last_name,
          first_name: form.first_name,
        },
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        },
      );
      navigate("/auth/sign_in");
    } catch (error) {
      if (error.response) {
        setError(error.response.data.error);
      } else {
        setError(error.message);
      }
    }
  }

  function handleForm(e: React.ChangeEvent<HTMLInputElement>): void {
    const id = e.target.id;
    const value = e.target.value;
    setForm({ ...form, [id]: value });
  }

  return { form, error, handleForm, submitForm };
}

interface FormForget {
  email: string;
}

export function useFormForget() {
  const [form, setForm] = useState<FormForget>({
    email: "",
  });

  const navigate = useNavigate();

  async function submitForm(e: any): Promise<void> {
    e.preventDefault();
    if (!form.email) {
      return;
    }

    const LOGINURL = `${process.env.REACT_APP_API_URL}/api/v1/forget`;
    try {
      const response = await axios.post(
        LOGINURL,
        {
          email: form.email,
        },
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        },
      );
      navigate("/auth/sign_in");
    } catch (error) {}
  }

  function handleForm(e: React.ChangeEvent<HTMLInputElement>): void {
    const id = e.target.id;
    const value = e.target.value;
    setForm({ ...form, [id]: value });
  }

  return { form, handleForm, submitForm };
}

export const UserContext = createContext({
  email: "",
  first_name: "",
  last_name: "",
});
