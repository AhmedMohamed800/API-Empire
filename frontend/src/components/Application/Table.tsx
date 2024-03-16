import React from "react";
const arrow = require("../../assets/apis/arrow.svg") as string;

const Table = ({ header, content, generateUUID }) => {
  return (
    <table className="bg-black">
      <thead>
        <tr className="tr">
          {header.map((head) => {
            return (
              <th
                key={head}
                className={`td  ${head.length <= 3 ? "uppercase" : "capitalize"}`}
              >
                {head}
              </th>
            );
          })}
        </tr>
      </thead>
      <tbody>
        {content.map((data) => {
          return (
            <tr key={generateUUID()} className="tr">
              {header.map((key) => (
                <td className="td" key={generateUUID()}>
                  {data[key]}
                </td>
              ))}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};

export default Table;
