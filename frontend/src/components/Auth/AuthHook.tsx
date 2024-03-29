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
  const [isLoading, setIsLoading] = useState(false);

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
    if (!form.email || !form.password || isLoading) {
      return;
    }
    setIsLoading(true);
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
      setIsLoading(false);
    } catch (error) {
      if (error.response) {
        setError(error.response.data.error);
      } else {
        setError(error.message);
      }
      setIsLoading(false);
    }
  }

  function handleForm(e: React.ChangeEvent<HTMLInputElement>): void {
    const id = e.target.id;
    const value =
      e.target.type === "checkbox" ? e.target.checked : e.target.value;
    setForm({ ...form, [id]: value });
  }

  return { form, error, handleForm, submitForm, isLoading };
}

type FormUP = {
  first_name: string;
  last_name: string;
  email: string;
  password: string;
};

export function useFormUP() {
  const [isLoading, setIsLoading] = useState(false);

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
    if (
      !form.email ||
      !form.password ||
      !form.first_name ||
      !form.last_name ||
      isLoading
    ) {
      return;
    }
    setIsLoading(true);
    const LOGINURL = `${process.env.REACT_APP_API_URL}/signup`;
    try {
      const response = await axios.post(LOGINURL, {
        email: form.email,
        password: form.password,
        last_name: form.last_name,
        first_name: form.first_name,
      });

      navigate("/auth/sign_in", {
        state: { message: response.data.Message },
      });
      setIsLoading(false);
    } catch (error) {
      if (error.response) {
        setError(error.response.data.error);
      } else {
        setError(error.message);
      }
      setIsLoading(false);
    }
  }

  function handleForm(e: React.ChangeEvent<HTMLInputElement>): void {
    const id = e.target.id;
    const value = e.target.value;
    setForm({ ...form, [id]: value });
  }

  return { form, error, handleForm, submitForm, isLoading };
}

interface FormForget {
  email: string;
}

export function useFormForget() {
  const [form, setForm] = useState<FormForget>({
    email: "",
  });
  const [error, setError] = useState<boolean>(false);

  const navigate = useNavigate();

  async function submitForm(e: any): Promise<void> {
    e.preventDefault();
    if (!form.email) {
      return;
    }
    try {
      const LOGINURL = `${process.env.REACT_APP_API_URL}/forgot_password`;
      const response = await axios.post(LOGINURL, {
        email: form.email,
      });
      navigate("/auth/sign_in");
    } catch (error) {
      console.log(error);
      setError(true);
    }
  }

  function handleForm(e: React.ChangeEvent<HTMLInputElement>): void {
    const id = e.target.id;
    const value = e.target.value;
    setForm({ ...form, [id]: value });
  }

  return { form, handleForm, submitForm, error };
}

interface FormReset {
  password: string;
  token: string | undefined;
  passwordConfirm: string;
}

export function useFromReset() {
  const [form, setForm] = useState<FormReset>({
    password: "",
    passwordConfirm: "",
    token: "",
  });

  const [error, setError] = useState<string>("");

  const navigate = useNavigate();

  async function submitForm(e: any): Promise<void> {
    setError("");
    e.preventDefault();
    if (
      !form.password ||
      !form.passwordConfirm ||
      form.password !== form.passwordConfirm
    ) {
      setError("The two passwords should be identical");
    }

    try {
      const LOGINURL = `${process.env.REACT_APP_API_URL}/api/v1/reset`;
      const response = await axios.post(
        LOGINURL,
        {
          password: form.password,
        },
        {
          headers: {
            "reset-token": form.token,
          },
        },
      );
      navigate("/auth/sign_in");
    } catch (error) {
      console.log(error);
    }
  }

  function handleForm(e: React.ChangeEvent<HTMLInputElement>): void {
    const id = e.target.id;
    const value = e.target.value;
    setForm({ ...form, [id]: value });
  }

  return { form, handleForm, submitForm, setForm, error };
}

export const UserContext = createContext({
  email: "",
  first_name: "",
  last_name: "",
});
