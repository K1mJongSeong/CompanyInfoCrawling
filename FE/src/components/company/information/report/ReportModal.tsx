"use client";

import RepoerPDF from "@/components/company/information/report/RepoerPDF";
import { PDFViewer } from "@react-pdf/renderer";
import {
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  Slide,
  IconButton,
} from "@mui/material";
import { forwardRef } from "react";
import { TransitionProps } from "@mui/material/transitions";
import CloseIcon from "@mui/icons-material/Close";
import { StyledDialog } from "./styles";

export interface DialogTitleProps {
  id: string;
  children?: React.ReactNode;
  onClose: () => void;
}

function BootstrapDialogTitle(props: DialogTitleProps) {
  const { children, onClose, ...other } = props;

  return (
    <DialogTitle sx={{ m: 0, p: 2 }} {...other}>
      {children}
      {onClose ? (
        <IconButton
          aria-label="close"
          onClick={onClose}
          sx={{
            position: "absolute",
            right: 8,
            top: 8,
            color: (theme) => theme.palette.grey[500],
          }}
        >
          <CloseIcon />
        </IconButton>
      ) : null}
    </DialogTitle>
  );
}

const Transition = forwardRef(function Transition(
  props: TransitionProps & {
    children: React.ReactElement<any, any>;
  },
  ref: React.Ref<unknown>
) {
  return <Slide direction="up" ref={ref} {...props} />;
});

interface Props {
  open: boolean;
  close: () => void;
}

export default function ReportModal({ open, close }: Props) {
  return (
    <StyledDialog
      open={open}
      TransitionComponent={Transition}
      keepMounted
      onClose={close}
      aria-describedby="alert-dialog-slide-description"
    >
      <BootstrapDialogTitle id="customized-dialog-title" onClose={close}>
        Report
      </BootstrapDialogTitle>
      <DialogContent>
        {/** render pdf */}
        <PDFViewer>
          <RepoerPDF />
        </PDFViewer>
      </DialogContent>
      <DialogActions>
        <Button onClick={close}>download</Button>
      </DialogActions>
    </StyledDialog>
  );
}
