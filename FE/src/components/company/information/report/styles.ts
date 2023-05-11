import styled from "@emotion/styled";
import { Dialog } from "@mui/material";

export const StyledDialog = styled(Dialog)`
  .MuiPaper-root {
    max-width: none;
    width: 100%;
    .MuiDialogContent-root {
      iframe {
        width: 100%;
        min-height: 500px;
        height: 700px;
      }
    }
  }
`;
