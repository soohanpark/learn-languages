import { useState, useEffect } from "react";

import Button from "./Button";
import styles from "./App.module.css";
import AppCleanUp from "./App_cleanUp";

function App() {
  const [counter, setValue] = useState(0);
  const [keyword, setKeyword] = useState("");

  console.log("i run all the time");

  const onClick = () => setValue((prev) => prev + 1);
  const onChange = (event) => setKeyword(event.target.value);

  useEffect(() => {
    console.log("i run only once");
  }, []);
  useEffect(() => {
    if (keyword !== "" && keyword.length > 5)
      console.log("I run when 'keyword' changes.");
  }, [keyword]);
  useEffect(() => {
    console.log("I run when 'counter' changes.");
  }, [counter]);
  useEffect(() => {
    console.log("I run when 'keyword' & 'counter' changes.");
  }, [counter, keyword]); // 둘다 동시에 변할때가 아니라, 둘 중 하나라도 변동이 있을때 실행됨!
  return (
    <div>
      <input
        value={keyword}
        type="text"
        placeholder="Search here..."
        onChange={onChange}
      />
      <h1 className={styles.title}>{counter}</h1>
      <button onClick={onClick}>Click Me</button>
      <Button text="Continue" />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <AppCleanUp />
    </div>
  );
}

export default App;
