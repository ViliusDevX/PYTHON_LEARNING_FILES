def display_popup(self, text):
    box_layout = MDBoxLayout(orientation='vertical', adaptive_height=True, spacing=10)

    answers_list = text.split('\n')
    my_items = [JobListItem(text=item) for item in answers_list]

    for item in my_items:
        box_layout.add_widget(item)

    dialog = MDDialog(
        title="Here are some jobs that suit you:",
        type="custom",  # <- Šito būtinai reikia jeigu darom custom dalykus
        # Height nurodymas pačiam dialog'ui neveikia, gali tik scrollview
        content_cls=ScrollView(height=dp(300)),
    )

    dialog.content_cls.add_widget(box_layout)
    # šitas perskaičiuoja dialog'o aukštį, nes apparently jis pats negali to padaryt
    # most likely anksčiau nematėm label'ų būtent dėl to
    dialog.update_height()
    dialog.open()