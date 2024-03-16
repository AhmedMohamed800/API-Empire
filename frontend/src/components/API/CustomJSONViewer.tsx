import React from "react";

const CustomJSONViewer = ({ data }) => {
  const renderJSON = (obj, indent = 0) => {
    const keys = Object.keys(obj);
    return (
      <div>
        <span>{"{"}</span>

        {keys.map((key, index) => (
          <div key={key} style={{ marginLeft: `${indent + 1 * 20}px` }}>
            <span style={{ color: "#61dafb" }}>"{key}": </span>
            {typeof obj[key] === "object" ? (
              <div>{renderJSON(obj[key], indent + 1)}</div>
            ) : (
              <span>{JSON.stringify(obj[key])},</span>
            )}
          </div>
        ))}
        <span>{"{"}</span>
      </div>
    );
  };

  return (
    <div>
      {typeof data === "object" ? (
        <div>{renderJSON(data)}</div>
      ) : (
        <span style={{ color: "#61dafb" }}>Invalid JSON data</span>
      )}
    </div>
  );
};

export default CustomJSONViewer;
