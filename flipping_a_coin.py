from manimlib.imports import *
import manimlib
import random

GLOBAL_CONFIG = {
    "camera_config": {"background_color": "#282c34"},
    "font": "Dank Mono"
}


class SceneOne(Scene):
    CONFIG = GLOBAL_CONFIG

    def construct(self):
        # Create question
        line_1 = Text("Write a program to flip", font="Dank Mono", stroke_width=0, size=1.7)
        line_2 = Text("a coin 6 million times and", font="Dank Mono", stroke_width=0, size=1.7)
        line_3 = Text("store the result of each toss.", font="Dank Mono", stroke_width=0, size=1.7)

        # Shift the statements
        line_1.shift(UP)
        line_3.shift(DOWN)

        # Write to the final render
        self.play(Write(line_1))
        self.play(Write(line_2))
        self.play(Write(line_3))
        self.wait(1)
        self.play(FadeOut(line_1), FadeOut(line_2), FadeOut(line_3))


class SceneTwo(Scene):
    CONFIG = GLOBAL_CONFIG

    def construct(self):
        # Intialise coin faces
        def init_coin_faces(coin_type, axis_shift=[0, 0, 0]):
            if isinstance(coin_type, list):
                return [init_coin_faces(coin_face, axis_shift) for coin_face in coin_type]
            if coin_type == "H":
                # return Circle().add(Text("Heads")).set_fill('#FAFAFA')
                return Circle().set_fill("#abb2bf", opacity=1).set_stroke("#C679DD", opacity=1).shift(axis_shift), Text(
                    "Heads").shift(axis_shift)
            else:
                return Circle().set_stroke("#C679DD", opacity=1).shift(axis_shift), Text("Tails").shift(axis_shift)

        # Initialise randomly outcomes
        outcomes = init_coin_faces(['H', 'T'])

        # Loop through random sequence
        for i, outcome in enumerate(outcomes):
            try:
                outcome[0].add(outcome[1])
                self.play(ShowCreation(outcome[0]))
                if i != 0:
                    self.remove(outcomes[i - 1][0])
                else:
                    pass
                break_checker = outcomes[i + 1][0]
                self.play(FadeOut(outcome[0].submobjects[0]))
                outcome[0].remove(outcome[0].submobjects[0])
                outcome[0].flip(X_AXIS)
                self.play(Transform(outcome[0], outcomes[i + 1][0]))
            except IndexError:
                self.wait(2)
                self.play(outcome[0].shift, [-4, 0, 0])
                final_coin = outcome
                # self.play(FadeOut(outcome[0]))

        # ===== Scene 3 =====
        outcomes = init_coin_faces(random.choices(['H', 'T'], k=1), [-4, 0, 0])
        outcomes.insert(0, final_coin)

        # Object initialisation
        arrow_p = Arrow(start=[3, 0, 0], end=[-3, 0, 0])
        mill_text = Text("Six Million", stroke_width=0).shift([4, 0, 0])
        mill_text_3 = TextMobject('X', stroke_width=2, size=2).shift([3.5, 0, 0])
        mill_text_4 = TextMobject('X Times', stroke_width=0, size=2).shift(1.5 * UP)
        mill_text_5 = Text('Randomness', stroke_width=0).shift(1.5 * UP)

        self.play(ShowCreation(arrow_p))
        self.play(ShowCreation(mill_text))

        for i, outcome in enumerate(outcomes):
            try:
                # ==== ALL BREAKING SHENANEGANS =====
                if i == 1:  # Make Arrow
                    self.play(Transform(mill_text, mill_text_3))
                # ===== END BREAKING SHENANEGANS =====
                outcome[0].add(outcome[1])
                if i == 0:
                    pass
                else:
                    if i == 1:
                        self.play(ShowCreation(outcome[0]), Transform(mill_text, mill_text_3))
                    else:
                        self.play(ShowCreation(outcome[0]))
                if i != 0:
                    self.remove(outcomes[i - 1][0])
                else:
                    pass
                break_checker = outcomes[i + 1][0]
                self.play(FadeOut(outcome[0].submobjects[0]))
                outcome[0].remove(outcome[0].submobjects[0])
                outcome[0].flip(X_AXIS)
                self.play(Transform(outcome[0], outcomes[i + 1][0]))
            except IndexError:
                # self.wait(2)
                self.remove(mill_text_3)
                self.play(FadeOut(arrow_p), ReplacementTransform(mill_text, mill_text_4), outcome[0].shift, [4, 0, 0])
                self.wait(2)
                self.play(Transform(mill_text_4, mill_text_5))
                final_coin = outcome

        outcomes = init_coin_faces(random.choices(['H', 'T'], k=2))
        outcomes.insert(0, final_coin)

        for i, outcome in enumerate(outcomes):
            try:
                outcome[0].add(outcome[1])
                if i == 0:
                    pass
                else:
                    self.play(ShowCreation(outcome[0]))
                if i != 0:
                    self.remove(outcomes[i - 1][0])
                else:
                    pass
                break_checker = outcomes[i + 1][0]
                self.play(FadeOut(outcome[0].submobjects[0]))
                outcome[0].remove(outcome[0].submobjects[0])
                outcome[0].flip(X_AXIS)
                self.play(Transform(outcome[0], outcomes[i + 1][0]))
            except IndexError:
                self.play(FadeOut(outcome[0]), FadeOut(mill_text_4))


class SceneTrials(Scene):
    CONFIG = GLOBAL_CONFIG

    def construct(self):
        # Create question
        import_t = Text("import", font="Dank Mono", stroke_width=0, color="#C679DD", slant=ITALIC)
        random_t = Text("random", font="Dank Mono", stroke_width=0, color="#C3D3DE")
        outcomes_t = Text("outcomes", font="Dank Mono", stroke_width=0, color="#C3D3DE")
        equals_t = Text("=", font="Dank Mono", stroke_width=0, color="#61AFEF")
        empty_list_t = Text("[]", font="Dank Mono", stroke_width=0, color="#C3D3DE")

        # Shift the statements
        import_t.to_edge(UP).shift([-1.5, 0, 0])
        random_t.move_to(import_t.get_center() + [1.9, 0.05, 0])
        outcomes_t.move_to(import_t.get_bottom() + [0.3, -0.3, 0])
        equals_t.move_to(outcomes_t.get_right() + [0.3, 0, 0])
        empty_list_t.move_to(equals_t.get_right() + [0.5, 0, 0])
        # line_3.shift(DOWN)

        # Write to the final render
        self.play(Write(import_t), Write(random_t))
        self.play(Write(outcomes_t), Write(equals_t), Write(empty_list_t))
        # self.play(Write(line_3))
        # self.wait(1)
        # self.play(FadeOut(line_1), FadeOut(line_2), FadeOut(line_3))


class SceneThree(Scene):
    CONFIG = GLOBAL_CONFIG

    def construct(self):
        coin_flip = Code(
            "coin_flip.py",
            tab_width=4,
            scale_factor=0.8,
            font="Dank Mono",
            insert_line_no=True,
            background="window",
            language="python",
            style="aod",
            size=6
        )
        debug_highlight = Rectangle(color="#FAFAFA", width=11, height=0.42).shift([0.32, 0.1, 0]).set_stroke(
            width=0).set_fill("#264b33", opacity=0.5).shift([0, 0.83, 0])

        self.play(FadeIn(coin_flip))
        self.play(ShowCreation(debug_highlight))
        self.play(debug_highlight.shift, [0, -0.43, 0])
        self.play(debug_highlight.shift, [0, -0.43, 0])
        self.play(debug_highlight.shift, [0, -0.43, 0])
        self.play(debug_highlight.shift, [0, -0.43, 0])
        self.play(debug_highlight.shift, [0, -0.43, 0])
