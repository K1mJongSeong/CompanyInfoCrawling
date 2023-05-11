"use client";
import {
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  Slide,
  IconButton,
} from "@mui/material";
import { forwardRef, useState } from "react";
import { TransitionProps } from "@mui/material/transitions";
import CloseIcon from "@mui/icons-material/Close";
import { StyledDialog } from "./styles";
import { PDFDownloadLink, PDFViewer } from "@react-pdf/renderer";
import RepoerPDF from "./RepoerPDF";
import Device from "@/components/common/Device";

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
        <Device>
          {({ isMobile }) => {
            if (isMobile) {
              return (
                <PDFDownloadLink document={<RepoerPDF />} fileName="My_Report">
                  {({ loading }) =>
                    loading ? (
                      "Loading..."
                    ) : (
                      <p className="align-center py-7">
                        Please use PC for PDF preview <br />
                        Click me to Download!
                      </p>
                    )
                  }
                </PDFDownloadLink>
              );
            }
            return (
              <PDFViewer>
                <RepoerPDF />
              </PDFViewer>
            );
          }}
        </Device>
      </DialogContent>
      <DialogActions>
        <PDFDownloadLink document={<RepoerPDF />} fileName="My_Report">
          {({ loading }) =>
            loading ? (
              "Loading..."
            ) : (
              <Button variant="contained" onClick={close}>
                download
              </Button>
            )
          }
        </PDFDownloadLink>
      </DialogActions>
    </StyledDialog>
  );
}
