import React from "react";
import axios from "axios";
import Cookies from "js-cookie";
import { useReducer, useContext, useRef, useState, useEffect } from "react";
import { UserContext } from "../components/Auth/AuthHook.tsx";
const edit = require("../assets/user/edit.svg") as string;

type State = {
  first_name: string;
  email: string;
  last_name: string;
  key: string;
};

type Action =
  | { type: "SET_FIRST_NAME"; payload: string }
  | { type: "SET_LAST_NAME"; payload: string }
  | { type: "SET_EMAIL"; payload: string }
  | { type: "SET_KEY"; payload: string };

interface key {
  key: string;
  message: string;
}

const User = () => {
  const [isCopied, setIsCopied] = useState(false);

  useEffect(() => {
    let timeoutId;
    if (isCopied) {
      timeoutId = setTimeout(() => setIsCopied(false), 2000);
    }
    return () => {
      if (timeoutId) {
        clearTimeout(timeoutId);
      }
    };
  }, [isCopied]);

  const { user, setUser } = useContext<any>(UserContext);
  const [key, setKey] = useState<key>({ key: "", message: "" });
  const [saved, setSaved] = useState(false);
  const firstNameRef = useRef<HTMLInputElement>(null);
  const lastNameRef = useRef<HTMLInputElement>(null);

  const initialState: State = {
    first_name: user.first_name,
    last_name: user.last_name,
    email: user.email,
    key: user.api_key,
  };
  function reducer(state: State, action: Action): State {
    switch (action.type) {
      case "SET_FIRST_NAME":
        return { ...state, first_name: action.payload };
      case "SET_LAST_NAME":
        return { ...state, last_name: action.payload };
      case "SET_EMAIL":
        return { ...state, email: action.payload };
      case "SET_KEY":
        return { ...state, key: action.payload };
      default:
        return state;
    }
  }
  const [state, dispatch] = useReducer(reducer, initialState);

  function getNewKey() {
    const session_id = Cookies.get("session");
    const KEYURL = `${process.env.REACT_APP_API_URL}/api/v1/get_key`;
    axios
      .post(KEYURL, {}, { headers: { "session-id": JSON.parse(session_id) } })
      .then((response) => {
        const { key, message } = response.data;
        setKey({ key, message });
        setTimeout(() => {
          setKey((ele) => {
            return { ...ele, message: "" };
          });
        }, 3000);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  function saveChanges(e) {
    e.preventDefault();
    const session_id = Cookies.get("session");
    const USERURL = `${process.env.REACT_APP_API_URL}/api/v1/user`;

    axios
      .put(
        USERURL,
        {
          first_name: state.first_name ? state.first_name : user.first_name,
          last_name: state.last_name ? state.last_name : user.last_name,
        },
        { headers: { "session-id": JSON.parse(session_id) } },
      )
      .then(() => {
        setUser({
          ...user,
          first_name: state.first_name ? state.first_name : user.first_name,
          last_name: state.last_name ? state.last_name : user.last_name,
        });
        setSaved(true);
        setTimeout(() => {
          setSaved(false);
        }, 1000);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  useEffect(() => {
    setKey((state) => {
      return { ...state, key: user.api_key };
    });
  }, [user.api_key]);

  return (
    <form
      onSubmit={saveChanges}
      className="z-10 mx-20 flex grow  flex-col   justify-center gap-6 max-md:mx-5 xl:mx-auto xl:w-[55%]"
    >
      <div className="flex gap-6">
        <label htmlFor="first_name" className="label relative grow">
          <span className="label_span">FIRST NAME</span>
          <input
            ref={firstNameRef}
            type="text"
            placeholder={user.first_name}
            id="first_name"
            name="first_name"
            value={state.first_name}
            autoComplete="none"
            className="input"
            disabled
            onChange={(e) => {
              dispatch({ type: "SET_FIRST_NAME", payload: e.target.value });
            }}
          />
          <img
            src={edit}
            alt="edit"
            width="24px"
            height="24px"
            className="absolute bottom-3 right-3 cursor-pointer hover:opacity-80"
            onClick={() => {
              if (firstNameRef.current) {
                firstNameRef.current.disabled = false;
              }
            }}
          />
        </label>
        <label htmlFor="last_name" className="label relative grow">
          <span className="label_span">LAST NAME</span>
          <input
            type="text"
            ref={lastNameRef}
            placeholder={user.last_name}
            id="last_name"
            name="last_name"
            value={state.last_name}
            autoComplete="none"
            className="input"
            disabled
            onChange={(e) => {
              dispatch({ type: "SET_LAST_NAME", payload: e.target.value });
            }}
          />
          <img
            src={edit}
            alt="edit"
            width="24px"
            height="24px"
            className="absolute bottom-3 right-3 cursor-pointer hover:opacity-80"
            onClick={() => {
              if (lastNameRef.current) {
                lastNameRef.current.disabled = false;
              }
            }}
          />
        </label>
      </div>
      <label htmlFor="email" className="label">
        <span className="label_span">EMAIL</span>
        <input
          type="email"
          placeholder={user.email}
          id="email"
          name="email"
          value={state.email}
          readOnly
          autoComplete="none"
          className="input"
          onChange={(e) => {
            dispatch({ type: "SET_EMAIL", payload: e.target.value });
          }}
        />
      </label>
      <div className="relative flex items-end gap-4 max-sm:flex-col max-sm:items-stretch">
        <div className="label grow">
          <span className="label_span">KEY</span>
          <p className="input">{key.key ? key.key : "There is no Key"}</p>
        </div>

        <div className="flex gap-4 max-sm:[&>button]:w-[50%]">
          <button
            type="button"
            className="mb-[1px] rounded-md bg-primary p-3 text-white hover:opacity-80"
            onClick={getNewKey}
          >
            Get New Key
          </button>
          <button
            type="button"
            className="mb-[1px] rounded-md bg-primary p-3 text-white hover:opacity-80"
            onClick={() => {
              navigator.clipboard.writeText(key.key);
              setIsCopied(true);
            }}
          >
            Copy
          </button>
        </div>
        <p
          className={`absolute top-[90px] text-green-500  max-sm:top-[155px] ${key.message || "hidden"}`}
        >
          {key.message}
        </p>
        {isCopied && (
          <p className=" absolute left-12 top-[3px] rounded-md bg-primary px-2 text-sm">
            Copied
          </p>
        )}
      </div>

      <button className="mt-5 rounded-md  bg-primary p-3 text-white hover:opacity-80">
        Save Changes
      </button>
      <p
        className={`relative bottom-3 text-center text-green-500 ${saved || "hidden"}`}
      >
        Your data has been updated
      </p>
    </form>
  );
};

export default User;
