const { createApp, ref } = Vue;

const App = {
    setup() {
        const metrics = ref([
            {
                label: "月間アクティブユーザー",
                value: "1,240",
                description: "先月比 +12.4%",
            },
            {
                label: "平均セッション時間",
                value: "5.3 min",
                description: "安定しています",
            },
            {
                label: "NPS スコア",
                value: "+32",
                description: "ユーザー満足度は良好です",
            },
        ]);

        const projects = ref([
            { name: "CPAP スマホアプリ API", status: "運用中", score: 89 },
            { name: "社内検索最適化", status: "改善中", score: 75 },
            { name: "ECS 移行プロジェクト", status: "完了", score: 92 },
        ]);

        return {
            metrics,
            projects,
        };
    },
};

createApp(App).mount("#app");
