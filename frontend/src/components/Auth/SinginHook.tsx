import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

type Form = {
  email: string;
  password: string;
  remember_me: boolean;
};

export function useForm() {
  const [form, setForm] = useState<Form>({
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
      document.cookie = `session=${JSON.stringify(session)}; path=/`;
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
