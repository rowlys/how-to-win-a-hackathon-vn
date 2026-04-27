label start:
    label state_loop:
        if current_state == State.START:
            call start_state
        elif current_state == State.CHOOSE_PROJECT:
            call choose_project_state

        elif current_state == State.HUB_EXPLORE:
            call hub_explore_state
        elif current_state == State.VISIT_RPL:
            call visit_rpl_state
        elif current_state == State.VISIT_KCV:
            call visit_kcv_state
        elif current_state == State.VISIT_GIGA:
            call visit_giga_state
        elif current_state == State.CHOOSE_LAB:
            call choose_lab_state
        elif current_state == State.ASSEMBLE_TEAM:
            call assemble_team_state

        else:
            return
        jump state_loop