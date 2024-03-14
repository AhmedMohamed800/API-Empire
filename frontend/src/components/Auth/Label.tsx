import React from "react";

interface LabelProps {
  id: string;
  type: string;
  placeholder?: string;
  name: string;
  handle: (e: React.ChangeEvent<HTMLInputElement>) => void;
  value: any;
}

const Label = ({ id, type, placeholder, name, handle, value }: LabelProps) => {
  if (type === "checkbox") {
    return (
      <label
        htmlFor={id}
        className="relative flex cursor-pointer items-center gap-2 "
      >
        <input
          type={type}
          id={id}
          value={value}
          onChange={handle}
          name={name}
          className="h-4 w-4 cursor-pointer appearance-none rounded-sm border-2   border-white checked:border-transparent  checked:bg-primary focus:outline-none "
        />
        <svg
          className="pointer-events-none absolute left-[3px] top-[4px] hidden  h-[12px] w-[11px] text-white"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path d="M0 11l2-2 5 5L18 3l2 2L7 18z" />
        </svg>
        <span className="text-sm font-bold text-primary">{name}</span>
      </label>
    );
  }

  return (
    <label htmlFor={id} className="label">
      <span className="label_span">{name}</span>
      <input
        type={type}
        placeholder={placeholder}
        id={id}
        name={name}
        value={value}
        required
        autoComplete="none"
        className="input"
        onChange={handle}
      />
    </label>
  );
};

export default Label;
