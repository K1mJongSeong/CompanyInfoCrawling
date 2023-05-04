import styled from "@emotion/styled";
import { Box, Button, Container } from "@mui/material";
import { deepPurple } from "@mui/material/colors";

export const AuthContainer = styled(Container)`
  padding: 80px 1rem;
  height: max-content;
`;

export const AuthCard = styled(Box)`
  border-radius: 10px;
  background-color: white;
  border: 1px solid ${deepPurple[300]};
  box-shadow: 4px 4px 20px rgba(23, 33, 122, 0.3);
  padding: 50px 1.5rem;
`;
export const AuthLoginBtn = styled(Button)`
  width: 100%;
  max-width: 192px;
  margin-bottom: 50px
`;
