import React from "react";
import { initialize, attachAuthListener } from "../utils/firebase";

export const authStates = {
  INITIAL_VALUE: "unknown",
  LOGGED_IN: "logged_in",
  LOGGED_OUT: "logged_out",
};

export function withAuth(WrappedComponent) {
  return class extends React.Component {
    state = {
      user: undefined,
      authState: authStates.INITIAL_VALUE,
    };

    componentDidMount() {
      // Initialize Firebase and set up the auth listener once the component is mounted
      initialize();
      this.unsubscribe = attachAuthListener((user) => {
        this.setState({
          user: user,
          authState: user ? authStates.LOGGED_IN : authStates.LOGGED_OUT,
        });
      });
    }

    componentWillUnmount() {
      // Remove the auth listener when the component unmounts
      if (this.unsubscribe) {
        this.unsubscribe();
      }
    }

    render() {
      // Pass down authState and user as props to the wrapped component
      return (
        <WrappedComponent
          authState={this.state.authState}
          user={this.state.user}
          {...this.props}
        />
      );
    }
  };
}
