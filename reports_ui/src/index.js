import { render } from 'react-dom';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import App from './App';
import Report from './routes/report';
import ReportList from './routes/reports_list';


const rootElement = document.getElementById('root')
render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />}>
        <Route path="daily" element={<ReportList />}>
          <Route
            index
            element={
              <main style={{ padding: "1rem" }}>
                <p>Select a report</p>
              </main>
            }
          />
          <Route path=":reportId" element={<Report />} />
        </Route>

        <Route path="monthly" element={<ReportList />}>
          <Route
            index
            element={
              <main style={{ padding: "1rem" }}>
                <p>Select a report</p>
              </main>
            }
          />
          <Route path=":reportId" element={<Report />} />
        </Route>

        <Route
          path="*"
          element={
            <main style={{ padding: "1rem" }}>
              <p>There's nothing here!</p>
            </main>
          }
        />
      </Route>
    </Routes>
  </BrowserRouter>,
  rootElement
);